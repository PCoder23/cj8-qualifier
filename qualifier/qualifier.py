  
from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:

    T = []
    Li = []
    Lb = []
    C = []
    B = []
    x = 0
    rows_length = []
    for n in rows[0]:
        rows_items = []
        p = 0
        for items in rows:
            p = p+1
            rows_items.append(str(items[x]))
        longest_string = max(rows_items, key=len)
        rows_length.append(longest_string)
        x = x+1
    
    if labels != None:
        y = 0
        for n in labels:
            if len(str(n)) > len(rows_length[y]):
                rows_length[y] = n
            y = y+1
    mal = []
    for n in rows_length:
        mal.append(len(str(n)))
    for maxL in mal[0:(len(mal)-1)]:
        t = "─"+"─"*maxL+"─"+"┬"
        l = "─"+"─"*maxL+"─"+"┼"
        b = "─"+"─"*maxL+"─"+"┴"
        T.append(t)
        B.append(b)
        if labels!= None and len(labels) > 0:
            Lb.append(l)   
    for maxL in mal[(len(mal)-1):]:
        t = "─"+"─"*maxL+"─"
        l = "─"+"─"*maxL+"─"
        b = "─"+"─"*maxL+"─"
        T.append(t)
        B.append(b)
        if labels != None and len(labels) > 0:
            Lb.append(l)
    if labels != None and len(labels)>0 and centered:
        p = 0
        for n in labels:
            maxL = mal[p]
            if (maxL%2) == 0 and len(str(n))%2 == 0: 
                spaces = " "*int(((maxL - len(str(n))))/2)
                e = " "
            elif (maxL%2) == 0 and len(str(n))%2 != 0:
                spaces = " "*int(((maxL - len(str(n))))/2 + 0.5)
                e = ""
            elif (maxL%2) != 0 and len(str(n))%2 == 0:
                spaces = " "*int(((maxL - len(str(n))))/2 + 0.5)
                e = ""
            else:
                spaces = " "*int(((maxL - len(str(n))))/2)
                e = " "
            cc = f"│ {spaces}{n}{spaces}{e}"
            crc = f"│ {spaces}{n}{spaces}{e}│\n"
            if n==labels[-1]:
                Li.append(crc)
            else:
                Li.append(cc)
            p = p+1
            r = 0
        for items in rows:
            p = 0
            for n in items:   
                maxL = mal[p]
                if (maxL%2) == 0 and len(str(n))%2 == 0: 
                    spaces = " "*int(((maxL - len(str(n))))/2)
                    e = " "
                elif (maxL%2) == 0 and len(str(n))%2 != 0:
                    spaces = " "*int(((maxL - len(str(n))))/2 + 0.5)
                    e = ""
                elif (maxL%2) != 0 and len(str(n))%2 == 0:
                    spaces = " "*int(((maxL - len(str(n))))/2 + 0.5)
                    e = ""
                else:
                    spaces = " "*int(((maxL - len(str(n))))/2)
                    e = " "
                cc = f"│ {spaces}{n}{spaces}{e}"
                crc = f"│ {spaces}{n}{spaces}{e}│\n"
                if n == rows[r][-1]:
                    C.append(crc)
                else:
                    C.append(cc)
                p = p+1
            r = r+1
    elif labels!=None and len(labels)>0:
        p = 0
        for n in labels:
            maxL = mal[p]
            spaces = " "*(maxL - len(str(n)))
            c = f"│ {n}{spaces} "
            cr = f"│ {n}{spaces} │\n"
            if n==labels[-1]:
                Li.append(cr)
            else:
                Li.append(c)
            p = p+1
        r = 0
        for items in rows:
            p = 0
            for n in items:
                maxL = mal[p]
                spaces = " "*(maxL - len(str(n)))
                c = f"│ {n}{spaces} "
                cr = f"│ {n}{spaces} │\n"
                if n == rows[r][-1]:
                    C.append(cr)
                else:
                    C.append(c)
                p = p+1
            r = r+1
    elif centered:
        r = 0
        for items in rows:
            p = 0
            for n in items:   
                maxL = mal[p]
                if (maxL%2) == 0 and len(str(n))%2 == 0: 
                    spaces = " "*int(((maxL - len(str(n))))/2)
                    e = " "
                elif (maxL%2) == 0 and len(str(n))%2 != 0:
                    spaces = " "*int(((maxL - len(str(n))))/2 + 0.5)
                    e = ""
                elif (maxL%2) != 0 and len(str(n))%2 == 0:
                    spaces = " "*int(((maxL - len(str(n))))/2 + 0.5)
                    e = ""
                else:
                    spaces = " "*int(((maxL - len(str(n))))/2)
                    e = " "
                cc = f"│ {spaces}{n}{spaces}{e}"
                crc = f"│ {spaces}{n}{spaces}{e}│\n"
                if n == rows[r][-1]:
                    C.append(crc)
                else:
                    C.append(cc)
                p = p+1
            r = r+1
    else:
        r = 0
        for items in rows:
            p = 0
            for n in items:
                maxL = mal[p]
                spaces = " "*(maxL - len(str(n)))
                c = f"│ {n}{spaces} "
                cr = f"│ {n}{spaces} │\n"
                if n == rows[r][-1]:
                    C.append(cr)
                else:
                    C.append(c)
                p=p+1
            r = r+1
    
    if labels == None:
        return "┌" +"".join(T) + "┐"+"\n"+"".join(C)+"└"+"".join(B) + "┘"
    else:
        return "┌" +"".join(T)  + "┐"+"\n" + "".join(Li)+"├"+"".join(Lb)+"┤"+"\n"+"".join(C)+"└"+"".join(B) + "┘"
