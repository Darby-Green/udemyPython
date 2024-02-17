def phoneBill (m,tx):
    m1 = ((m-50)*0.25)
    tx1 = ((tx-50)*0.15)
    ph1 =  m1 + tx1 + 15.00 + 0.44
    ph2 = tx1 + 15.00 + 0.44
    ph3 = m1 + 15.00 + 0.44
    tax = ph1 * 0.05
    total1 = tax + ph1
    tax2 = ph2 * 0.05
    total2 = tax2 + ph2
    tax3 = ph3 * 0.05
    total3 = ph3 + tax3
    if m < 50:
        return total2
    elif tx < 50:
        return total3
    else:
        return total1



