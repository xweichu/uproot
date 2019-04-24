import uproot
# values = uproot.open("/test/HZZ.root").keys()
hzz = uproot.open("/test/HZZ.root")["events"]
# values = uproot.open("http://scikit-hep.org/uproot/examples/HZZ.root").keys()
print(hzz.keys())