
import hashlib
from optparse import OptionParser
import sys

# Prints usage syntax
def helpMenu():
    print("Dehasher: A python hash cracker utility, by Pratik Das [NEU ID: 001037548]")
    print("Usage: python %s -H <hash value to crack> -t <hash type of the provided hash> -l <password list>" % sys.argv[0])
    print("Example: python %s -H d8611198ea8421180df8e80eab0f2da1 -t md5 -l mypasslist.txt" % sys.argv[0])

# Generates hash of the corresponding plaintext 
def generateHash(content, hashAlg):
    hInst = hashlib.new(hashAlg)
    hInst.update(content.encode('utf-8'))
    return hInst.hexdigest()

# Returns list of hash algorithms supported
def getSupportedhTypes():
    return hashlib.algorithms_guaranteed


# Standard function to check argument's validity
def argChecks(hValue, hType, passFile):
    # Check if all arguments are present
    if not (hValue and hType and passFile):
        helpMenu()
        exit(0)

    # Check if the supplied hashing algorithm is in the list of supported hashing algorithm
    if hType not in getSupportedhTypes():
        print(f"Invalid hash type: {hType}")
        print("Supported hash types are - ", ", ".join(getSupportedhTypes()))
        exit(0)

def mainFunction():
    # Parsing commandline arguments
    usageSyntax = """
# Syntax:
    python %s -H <hash value to crack> -t <hash type of the provided hash> -l <password list>
# Example:
    python %s -H d8611198ea8421180df8e80eab0f2da1 -t md5 -l mypasslist.txt
""" % (sys.argv[0], sys.argv[0])
    optHndl = OptionParser(usageSyntax)
    optHndl.add_option("-H", dest="hValue", type="string", help="Hash value to crack")
    optHndl.add_option("-t", dest="hType", type="string", help="Hash type of the provided hash. For e.g. - md5, sha1")
    optHndl.add_option("-l", dest="passFile", type="string", help="Path to password list")
    (script_opts, argsList) = optHndl.parse_args()

    # Invoking argument check
    argChecks(script_opts.hValue, script_opts.hType, script_opts.passFile)

    # Starting the hash cracking operations
    print("Perform hash cracking operations for \"%s\" hash (%s hash) ..." % (script_opts.hValue, script_opts.hType))

    # Traverses password list line-by-line, derives hash value for each and compares it with the provided hash value
    # If it matches, then print the corresponding plaintext.
    with open(script_opts.passFile, 'r') as passlist:
        for wrd in passlist:
            wrd = wrd.strip("\n")
            calculated_hash = generateHash(wrd, script_opts.hType)
            if script_opts.hValue == calculated_hash:
                print(f"\n[+] Hash Found - [ {wrd} ]")
                exit(0)

    print("\n[-] Hash not found\n")

# Program entrypoint
if __name__ == "__main__":
    mainFunction()