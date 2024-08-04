#!/usr/bin/python3

import time, os, json, psutil;

class Resource():
    def __init__(self, name, type):
        self.date = time.time()
        self.name = name
        self.type = type

    def printTimestamp(self):
        return str(self.date)

    def printName(self):
        return str(self.name)

    def printType(self):
        return str(self.type)

class CPUResource(Resource):
    def getCpuLoad(self):
        return psutil.cpu_percent()


class MEMResource(Resource):
    def gerMemoryLoad(self):
        return psutil.virtual_memory().percent


if __name__ == '__main__':
    testCPU = CPUResource("CPU load", "CPU")
    testMEM = MEMResource("MEM load", "MEM")

    print(str(testCPU.getCpuLoad()))
    print(testCPU.printType())
