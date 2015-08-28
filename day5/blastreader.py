class BLASTReader(object):
    def __init__(self, file):
        self.file = open(file)
        self.last_ident = None  
        
    def next(self):
        if self.last_ident is None:
            line = self.file.readline()
            #assert line.startswith(">"), "Not valid fasta"
            ident = line[1:].rstrip("\r\n") #if either of these characters occur at the end of the string, remove them and return rest of the string. lstrip works for the left of the string, strip for both. 
        else:
            ident = self.last_ident 

        sequences = []
        while True: #while loops loop as long as the command is true 
            line = self.file.readline()
            if not line:
                break
            if line.startswith(">"):
                self.last_ident = line[1:].rstrip(">")
                sequences.append(line.strip())
            if line.startswith(" Identities"):
                sequences.append(line.strip())
                break
                
        if len(sequences) == 0:
            raise StopIteration 
    
        sequence = "".join(sequences)

        return ident, sequence
    
    def __iter__(self):
        return self