import asyncio
import struct
from typing import List, Tuple
from pymem import pymem
from pymem.process import module_from_name
from CommonClient import logger

class Rb3MemoryInterface():
    """Rb3MemoryInterface allows for reading and writing to the Rb3 game memory."""

    def __init__(self):
        self.rb3_memory = None
        self.rb3_processID = None
        self.vfszTreasureData = [[0x089D, 1 << 3], [0x89D, 1 << 4], [0x89D, 1 << 5], [0x89D, 1 << 6]]
        self.stationAreaTreasureData = [[0x089E, 1 << 5], [0x89E, 1 << 6], [0x89E, 1 << 7], [0x89F, 1]]
        self.vfszTreasureFlags = [0,0,0,0]
        self.stationAreaTreasureFlags = [0,0,0,0]

    def is_connected(self):
        if self.rb3_memory is None:
            return False
        
        return True

    
    def _read_byte(self, offset):
        """
        Read 1 byte of data at <base_process_address> + offset and return it.

        :int offset: the offset to read data from.
        """
        data = self.rb3_memory.read_bytes(self.rb3_savePointer + offset, 1)
        converted_data = int.from_bytes(data, byteorder="little", signed=False)
        return converted_data
    
    async def connect(self, exit_event: asyncio.Event):
        try:
            self.rb3_memory = pymem.Pymem("NeptuniaReBirth3.exe")
            self.rb3_processID = self.rb3_memory.process_id
            self.rb3_baseAddress = module_from_name(self.rb3_memory.process_handle, "NeptuniaReBirth3.exe").lpBaseOfDll
            self.rb3_basePointer = self.rb3_memory.read_int(self.rb3_baseAddress)
            self.rb3_savePointer = self.rb3_memory.read_int(self.rb3_baseAddress + 0x4F6ED8)

        except pymem.exception.ProcessNotFound:
            await asyncio.sleep(3)


    
