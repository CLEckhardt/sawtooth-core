# Copyright 2017 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------

import logging

from sawtooth_validator.protobuf import validator_pb2
from sawtooth_validator.networking.dispatch import Handler
from sawtooth_validator.networking.dispatch import HandlerResult
from sawtooth_validator.networking.dispatch import HandlerStatus

from sawtooth_validator.protobuf.events_pb2 \
    import ClientEventsSubscribeRequest
from sawtooth_validator.protobuf.events_pb2 \
    import ClientEventsSubscribeResponse
from sawtooth_validator.protobuf.events_pb2 \
    import ClientEventsUnsubscribeRequest
from sawtooth_validator.protobuf.events_pb2 \
    import ClientEventsUnsubscribeResponse

from sawtooth_validator.server.events.subscription import EventSubscription
from sawtooth_validator.server.events.subscription import EventFilterFactory
from sawtooth_validator.server.events.subscription import InvalidFilterError

LOGGER = logging.getLogger(__name__)


class ClientEventsSubscribeValidationHandler(Handler):
    """Handles validating an EventSubscriptionRequest. This must be done
    separately from adding the subscriber to the EventBroadcaster so that the
    subscriber does not receive events before the EventSubscribeResponse.
    """

    _msg_type = validator_pb2.Message.CLIENT_EVENTS_SUBSCRIBE_RESPONSE

    def __init__(self, event_broadcaster):
        self._event_broadcaster = event_broadcaster
        self._filter_factory = EventFilterFactory()

    def handle(self, connection_id, message_content):
        request = ClientEventsSubscribeRequest()
        request.ParseFromString(message_content)

        ack = ClientEventsSubscribeResponse()
        try:
            subscriptions = [
                EventSubscription(
                    event_type=sub.event_type,
                    filters=[
                        self._filter_factory.create(
                            f.key, f.match_string, f.filter_type)
                        for f in sub.filters
                    ],
                )
                for sub in request.subscriptions
            ]
        except InvalidFilterError as err:
            LOGGER.warning("Invalid Filter Error: %s", err)
            ack.status = ack.INVALID_FILTER
            ack.response_message = str(err)
            return HandlerResult(
                HandlerStatus.RETURN,
                message_out=ack,
                message_type=self._msg_type)

        self._event_broadcaster.add_subscriber(
            connection_id, subscriptions, request.last_known_block_ids)

        ack.status = ack.OK
        return HandlerResult(
            HandlerStatus.RETURN_AND_PASS,
            message_out=ack,
            message_type=self._msg_type)


class ClientEventsSubscribeHandler(Handler):
    """Tells the EventBroadcaster to actually start sending the subscriber
    events. This is separate from validation and acknowledgement in order to
    ensure the correct message ordering.
    """

    def __init__(self, event_broadcaster):
        self._event_broadcaster = event_broadcaster

    def handle(self, connection_id, message_content):
        self._event_broadcaster.enable_subscriber(connection_id)
        return HandlerResult(HandlerStatus.PASS)


class ClientEventsUnsubscribeHandler(Handler):
    _msg_type = validator_pb2.Message.CLIENT_EVENTS_UNSUBSCRIBE_RESPONSE

    def __init__(self, event_broadcaster):
        self._event_broadcaster = event_broadcaster

    def handle(self, connection_id, message_content):
        request = ClientEventsUnsubscribeRequest()
        request.ParseFromString(message_content)

        ack = ClientEventsUnsubscribeResponse()
        self._event_broadcaster.disable_subscriber(connection_id)
        self._event_broadcaster.remove_subscriber(connection_id)

        ack.status = ack.OK

        return HandlerResult(
            HandlerStatus.RETURN,
            message_out=ack,
            message_type=self._msg_type)
