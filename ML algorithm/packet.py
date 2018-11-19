# automatically generated by the FlatBuffers compiler, do not modify

# namespace: kmeans

import flatbuffers

class Packet(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPacket(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Packet()
        x.Init(buf, n + offset)
        return x

    # Packet
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Packet
    def Duration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Packet
    def ProtocolType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Packet
    def Service(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Packet
    def Flag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Packet
    def SrcBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Packet
    def DstBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Packet
    def Land(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Packet
    def WrongFragment(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Packet
    def Urgent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Packet
    def Hot(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Packet
    def Count(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Packet
    def SrvCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Packet
    def SerrorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Packet
    def SrvSerrorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Packet
    def RerrorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Packet
    def SrvRerrorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Packet
    def SameSrvRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Packet
    def DiffSrvRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Packet
    def SrvDiffHostRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Packet
    def DstHostCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Packet
    def DstHostSrvCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Packet
    def DstHostSameSrvRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Packet
    def DstHostDiffSrvRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Packet
    def DstHostSameSrcPortRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Packet
    def DstHostSrvDiffHostRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Packet
    def DstHostSerrorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Packet
    def DstHostSrvSerrorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Packet
    def DstHostRerrorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Packet
    def DstHostSrvRerrorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def PacketStart(builder): builder.StartObject(29)
def PacketAddDuration(builder, duration): builder.PrependInt32Slot(0, duration, 0)
def PacketAddProtocolType(builder, protocolType): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(protocolType), 0)
def PacketAddService(builder, service): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(service), 0)
def PacketAddFlag(builder, flag): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(flag), 0)
def PacketAddSrcBytes(builder, srcBytes): builder.PrependInt32Slot(4, srcBytes, 0)
def PacketAddDstBytes(builder, dstBytes): builder.PrependInt32Slot(5, dstBytes, 0)
def PacketAddLand(builder, land): builder.PrependInt32Slot(6, land, 0)
def PacketAddWrongFragment(builder, wrongFragment): builder.PrependInt32Slot(7, wrongFragment, 0)
def PacketAddUrgent(builder, urgent): builder.PrependInt32Slot(8, urgent, 0)
def PacketAddHot(builder, hot): builder.PrependInt32Slot(9, hot, 0)
def PacketAddCount(builder, count): builder.PrependInt32Slot(10, count, 0)
def PacketAddSrvCount(builder, srvCount): builder.PrependInt32Slot(11, srvCount, 0)
def PacketAddSerrorRate(builder, serrorRate): builder.PrependFloat32Slot(12, serrorRate, 0.0)
def PacketAddSrvSerrorRate(builder, srvSerrorRate): builder.PrependFloat32Slot(13, srvSerrorRate, 0.0)
def PacketAddRerrorRate(builder, rerrorRate): builder.PrependFloat32Slot(14, rerrorRate, 0.0)
def PacketAddSrvRerrorRate(builder, srvRerrorRate): builder.PrependFloat32Slot(15, srvRerrorRate, 0.0)
def PacketAddSameSrvRate(builder, sameSrvRate): builder.PrependFloat32Slot(16, sameSrvRate, 0.0)
def PacketAddDiffSrvRate(builder, diffSrvRate): builder.PrependFloat32Slot(17, diffSrvRate, 0.0)
def PacketAddSrvDiffHostRate(builder, srvDiffHostRate): builder.PrependFloat32Slot(18, srvDiffHostRate, 0.0)
def PacketAddDstHostCount(builder, dstHostCount): builder.PrependInt32Slot(19, dstHostCount, 0)
def PacketAddDstHostSrvCount(builder, dstHostSrvCount): builder.PrependInt32Slot(20, dstHostSrvCount, 0)
def PacketAddDstHostSameSrvRate(builder, dstHostSameSrvRate): builder.PrependFloat32Slot(21, dstHostSameSrvRate, 0.0)
def PacketAddDstHostDiffSrvRate(builder, dstHostDiffSrvRate): builder.PrependFloat32Slot(22, dstHostDiffSrvRate, 0.0)
def PacketAddDstHostSameSrcPortRate(builder, dstHostSameSrcPortRate): builder.PrependFloat32Slot(23, dstHostSameSrcPortRate, 0.0)
def PacketAddDstHostSrvDiffHostRate(builder, dstHostSrvDiffHostRate): builder.PrependFloat32Slot(24, dstHostSrvDiffHostRate, 0.0)
def PacketAddDstHostSerrorRate(builder, dstHostSerrorRate): builder.PrependFloat32Slot(25, dstHostSerrorRate, 0.0)
def PacketAddDstHostSrvSerrorRate(builder, dstHostSrvSerrorRate): builder.PrependFloat32Slot(26, dstHostSrvSerrorRate, 0.0)
def PacketAddDstHostRerrorRate(builder, dstHostRerrorRate): builder.PrependFloat32Slot(27, dstHostRerrorRate, 0.0)
def PacketAddDstHostSrvRerrorRate(builder, dstHostSrvRerrorRate): builder.PrependFloat32Slot(28, dstHostSrvRerrorRate, 0.0)
def PacketEnd(builder): return builder.EndObject()
