#!/usr/bin/env python3

def acronyms(s):
    s = s.strip(".")
    retval = []
    acr = ""
    for c in s:
        if c.isupper() or c.isdigit():
            acr += c
        else:
            if len(acr) >= 2:
                if not acr.isupper():
                    acr = ""
                    continue
                retval.append(acr)
                acr = ""
            else:
                acr = ""

    if not acr == "":
        retval.append(acr)
    return retval


def main():
    print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))


if __name__ == "__main__":
    main()
