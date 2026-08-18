from collections import defaultdict
import numpy as np
import sys

class Fort14():
    def __init__(self, fname):
        self.renum = {} # renum[n] gives the renumbered node number of n
        self.nbdv = defaultdict(list)
        self.nbvv = defaultdict(list)

        with open(fname) as f:
            line = f.readline()
            self.title = "_".join(line.split())
            line = f.readline().split()
            self.ne = int(line[0])
            self.np = int(line[1])

            self.xs = np.zeros(self.np)
            self.ys = np.zeros(self.np)
            self.bath = np.zeros(self.np)
            self.elems = np.zeros((self.ne, 3), dtype=np.int32)

            # loop through nodes
            for i in range(self.np):
                line = f.readline().split()
                self.renum[int(line[0])] = i+1
                self.xs[i] = float(line[1])
                self.ys[i] = float(line[2])
                self.bath[i] = float(line[3])

            # renumber the connectivity list
            # element numbers are already correctly numbered from 1 to NE
            for i in range(self.ne):
                line = f.readline().split()
                n1, n2, n3 = [self.renum[int(line[k])] for k in [2,3,4]]
                self.elems[i,:] = [n1, n2, n3]

            self.nope = int(f.readline().split()[0])
            self.neta = int(f.readline().split()[0])

            self.nvdll = np.zeros(self.nope, dtype=np.int32)
            self.ibtypee = np.zeros(self.nope, dtype=np.int32)

            for k in range(self.nope):
                line = f.readline().split()
                self.nvdll[k] = int(line[0])
                self.ibtypee[k] = int(line[1])
                for _ in range(self.nvdll[k]):
                    line = f.readline().split()
                    self.nbdv[k].append(self.renum[int(line[0])])

            self.nbou = int(f.readline().split()[0])
            self.nvel = int(f.readline().split()[0])
            self.nvell = np.zeros(self.nbou, dtype=np.int32)
            self.ibtype  = np.zeros(self.nbou, dtype=np.int32)

            for k in range(self.nbou):
                line = f.readline().split()
                self.nvell[k] = int(line[0])
                self.ibtype[k] = int(line[1])
                if self.ibtype[k] not in [0,1,2,10,11,12,20,21,22,30]:
                    print("ERROR: ibtype %d not supported!" % self.ibtype[k])
                    sys.exit()

                for _ in range(self.nvell[k]):
                    line = f.readline().split()
                    self.nbvv[k].append(self.renum[int(line[0])])

    def write(self, fname):
        with open(fname, 'w') as f:
            f.write(self.title + '\n')
            f.write(f"    {self.ne}    {self.np}\n")
            for i in range(self.np):
                f.write(f"  {i+1} {self.xs[i]} {self.ys[i]} {self.bath[i]}\n")

            for i in range(self.ne):
                f.write(f"  {i+1} 3 {self.elems[i,0]} {self.elems[i,1]} {self.elems[i,2]}\n" )

            f.write(f"{self.nope}  NOPE (number of open boundaries)\n")
            f.write(f"{self.neta}  NETA (total number of open boundary nodes)\n")
            for k in range(self.nope):
                f.write(f"  {self.nvdll[k]} {self.ibtypee[k]}  (no. of nodes, ibtype) of open boundary {k+1}\n")
                for j in range(self.nvdll[k]):
                    f.write(f"    {self.nbdv[k][j]}\n")

            f.write(f"{self.nbou}  NBOU (number of land boundaries)\n")
            f.write(f"{self.nvel}  NVEL (total number of land boundary nodes)\n")
            for k in range(self.nbou):
                f.write(f"    {self.nvell[k]} {self.ibtype[k]} (no. of nodes, ibtype) of land boundary {k+1}\n")
                for j in range(self.nvell[k]):
                    f.write(f"    {self.nbvv[k][j]}\n")
