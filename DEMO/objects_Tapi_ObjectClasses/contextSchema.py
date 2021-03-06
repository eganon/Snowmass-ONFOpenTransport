from notification import Notification
from virtualNetworkService import VirtualNetworkService
from topology import Topology
from notificationSubscriptionService import NotificationSubscriptionService
from serviceEndPoint import ServiceEndPoint
from pathComputationService import PathComputationService
from connectivityService import ConnectivityService
from globalClass import GlobalClass
from objects_common.keyedArrayType import KeyedArrayType

class ContextSchema(GlobalClass):

    def __init__(self, json_struct=None):
        self._notification=KeyedArrayType(Notification, 'notificationId')
        self._vnwService=KeyedArrayType(VirtualNetworkService, 'uuid')
        self._topology=KeyedArrayType(Topology, 'uuid')
        self._notifSubscription=KeyedArrayType(NotificationSubscriptionService, 'uuid')
        self._serviceEndPoint=KeyedArrayType(ServiceEndPoint, 'uuid')
        self._pathCompService=KeyedArrayType(PathComputationService, 'uuid')
        self._connectivityService=KeyedArrayType(ConnectivityService, 'uuid')
        super(ContextSchema, self).__init__(json_struct)

