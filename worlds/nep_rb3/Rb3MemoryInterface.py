import asyncio
import struct
from typing import List, Tuple
from pymem import pymem
from pymem.process import module_from_name
from CommonClient import logger
from . import offsets

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
        Read 1 byte of data in save data + offset and return it.

        :int offset: the offset to read data from.
        """
        data = self.rb3_memory.read_bytes(self.rb3_savePointer + offset, 1)
        converted_data = int.from_bytes(data, byteorder="little", signed=False)
        return converted_data
    
    def _read_short(self, offset):
        data = self.rb3_memory.read_bytes(self.rb3_savePointer + offset, 2)
        converted_data = int.from_bytes(data, byteorder="little", signed=False)
        return converted_data
    
    def _write_byte(self, offset, value):
        self.rb3_memory.write_char(self.rb3_savePointer + offset, value)
    
    def _write_short(self, offset, value):
        data = value.to_bytes(2, byteorder="little", signed=False)
        self.rb3_memory.write_bytes(self.rb3_savePointer + offset, data, 2)
    
    def _get_item_at_slot(self, slot):
        """
        Read what an item ID is at a specific inventory slot

        :int slot: the item slot to read, 2-bytes
        """
        slotOffsetToRead = offsets.INVENTORY_START + self._slot_to_offset(slot)
        return self._read_short(slotOffsetToRead)
    
    def _get_item_amount(self, slot):
        """
        Read how much of an item exists at a specific inventory slot

        :int slot: the item slot to read, 2-bytes
        """
        if not slot:
            return 0
        
        slotOffsetToRead = offsets.INVENTORY_START + self._slot_to_offset(slot) + offsets.ITEM_AMOUNT
        return self._read_byte(slotOffsetToRead)
    
    def insert_inventory_item(self, ID, amount):
        """
        Insert an item ID and count into the player's inventory. We first check if the item exists, and if it does, insert it there, otherwise insert it at the end of the inventory.
        """
        itemSlot = self._get_item_slot(ID)

        if itemSlot:
            self._insert_existing_item(itemSlot, amount)
            return
        
        self._insert_new_item(ID, amount)

    def _insert_new_item(self, ID, amount):
        """
        Inserts an item that doesn't exist in the inventory yet, then calls the function to increment the inventory size
        """
        freeItemSpace = self._slot_to_offset(self._current_item_count())
        amountOffset = freeItemSpace + offsets.ITEM_AMOUNT

        self._write_short(offsets.INVENTORY_START + freeItemSpace, ID)
        self._write_byte(amountOffset, amount)
        self._set_current_item_count(self._current_item_count() + 1)


    def _insert_existing_item(self, slot, amount):
        """
        Inserts an amount of an item into an already known inventory slot
        """

        offsetToWrite = offsets.INVENTORY_START + self._slot_to_offset(slot) + offsets.ITEM_AMOUNT
        newItemAmount = self._get_item_amount(slot) + amount

        self._write_byte(offsetToWrite, newItemAmount)

    def _get_item_slot(self, ID):
        loopCount = self._current_item_count()

        if loopCount == 0:
            return None
        
        for i in range(0, loopCount, 1):
            currentItemID = self._get_item_at_slot(i)

            if currentItemID == ID:
                return i
            
        return None


    def _slot_to_offset(self, slot):
        return slot * offsets.ITEM_LENGTH


    def _current_item_count(self):
        """
        Returns how big the inventory currently is
        """
        return self._read_short(offsets.INVENTORY_SIZE)

    def _set_current_item_count(self, count):
        """
        Tells the game how big to make the inventory, this is necessary for new items to appear properly
        """
        self._write_short(offsets.INVENTORY_SIZE, count)

    
    async def connect(self, exit_event: asyncio.Event):
        try:
            self.rb3_memory = pymem.Pymem("NeptuniaReBirth3.exe")
            self.rb3_processID = self.rb3_memory.process_id
            self.rb3_baseAddress = module_from_name(self.rb3_memory.process_handle, "NeptuniaReBirth3.exe").lpBaseOfDll
            self.rb3_basePointer = self.rb3_memory.read_int(self.rb3_baseAddress)
            self.rb3_savePointer = self.rb3_memory.read_int(self.rb3_baseAddress + 0x4F6ED8)

        except pymem.exception.ProcessNotFound:
            await asyncio.sleep(3)


    
