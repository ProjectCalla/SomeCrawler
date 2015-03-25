__author__ = 'j'
from somecrawler.queue import QueueManager
import SharedMemory
shared = SharedMemory.SharedMemory(1)
queue = QueueManager.QueueManager()