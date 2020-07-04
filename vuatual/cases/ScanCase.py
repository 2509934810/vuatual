from vuatual.core import BaseCase
import pytest
import socket
from vuatual.utils.exceptions import CaseFormatError


class ScanCase(BaseCase):
    def __init__(self, name, parent, caseItem, authConfig):
        super(BaseCase, self).__init__(name, parent)
        self.name = name
        self.caseItem = caseItem
        self.authConfig = authConfig

    def runtest(self):
        ipList = self.caseItem.get("ip")
        for ip in _parseIp(ipList):
            pass


GET_SOCKET = {
    "tcp": socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    "udp": socket.socket(socket.AF_INET, socket.SOCK_DGRAM),
}


def _parseIp(baseIp):
    ipType_1 = baseIp.split("-")
    ipType_2 = baseIp.split("/")
    ipList = []
    if len(ipType_1) == 2:
        startIp = ipType_1[0]
        stopIp = ipType_1[1]
        if isinstance(stopIp, int):
            assert int(startIp.split(".")[-1]) < int(stopIp)
            ipHead = ".".join(startIp.split(".")[:-1])
            ipTailList = [
                "{}.{}".format(ipHead, ipTail)
                for ipTail in range(int(startIp.split(".")[-1]), int(stopIp))
            ]
            return ipTailList
        else:
            raise CaseFormatError("case should like 192.168.124.1-24")
    if len(ipType_2) == 2:
        headIp = ipType_2[0]
        TailSize = int(ipType_2[1])
        ipByte = ipType_2[0].split(".")
        if TailSize == 24:
            ipHead = ".".join(headIp.split(".")[:-1])
            ipTailList = [
                "{}.{}".format(ipHead, ipTail)
                for ipTail in range(int(startIp.split(".")[-1]), int(stopIp))
            ]
            return ipTailList
        else:
            raise CaseFormatError("th ip range too big")
    else:
        return list(baseIp)


def getSocket(ip, port, type):
    try:
        conn = GET_SOCKET.get(type).connect((ip, port))
    except Exception as e:
        print(e)
    return conn
