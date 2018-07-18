from collections import defaultdict as dd

chicago_bears = {"QB": "Mitch Trubisky",
                 "RB": "Jordan Howard",
                 "Wide Receivers": ["Allen Robinson", "Kevin White", "Anthony Miller"],
                 "Tight Ends": ["Trey Burton", "Dion Simms", "Adam Shaheen"]
                }
print(chicago_bears["Wide Receivers"])

all_caps = {value.upper() for value in chicago_bears["Wide Receivers"]}
print(all_caps)

