import sys, os
binpath = '/'.join(os.path.realpath(__file__).split("/")[:-1])+'/bin'
sys.path.insert(1, binpath)
import license

if __name__ == '__main__':
    license.license_setup()
