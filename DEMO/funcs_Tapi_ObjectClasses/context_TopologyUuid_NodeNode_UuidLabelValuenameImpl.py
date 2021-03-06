import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_TopologyUuid_NodeNode_UuidLabelValuenameImpl:

    @classmethod
    def get(cls, uuid, node_uuid, valueName):
        print 'handling get'
        if uuid in Context._topology:
            if node_uuid in Context._topology[uuid]._node:
                if valueName in Context._topology[uuid]._node[node_uuid].label:
                    return Context._topology[uuid]._node[node_uuid].label[valueName]
                else:
                    raise KeyError('valueName')
            else:
                raise KeyError('node_uuid')
        else:
            raise KeyError('uuid')
