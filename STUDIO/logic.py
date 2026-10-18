from datetime import date

# Every operation returns (ok, message) and only changes data when ok is True.


def find(items, id):
    return next((x for x in items if x["id"] == id), None)


def out(data, eid):
    """Units currently borrowed = sum of this item's transactions still marked 'borrowed'."""
    return sum(t["quantity"] for t in data["transactions"]
               if t["equipment_id"] == eid and t["status"] == "borrowed")


def add(data, name, cat, qty):
    if not name or not cat or qty < 1:
        return False, "Name, category and a quantity of at least 1 are required."
    eid = data["next_eid"]  # counter, so an ID is never reused even after deletes
    data["next_eid"] += 1
    data["equipment"].append({"id": eid, "name": name, "category": cat, "quantity": qty})
    return True, f"Added '{name}' with ID {eid}."


def update(data, eid, name, cat, qty):
    eq = find(data["equipment"], eid)
    if not eq:
        return False, "Equipment not found."
    if qty is not None and (qty < 1 or qty < out(data, eid)):
        return False, "Total must be at least 1 and not less than the borrowed units."
    eq.update(name=name or eq["name"], category=cat or eq["category"], quantity=qty or eq["quantity"])
    return True, "Equipment updated."


def delete(data, eid):
    eq = find(data["equipment"], eid)
    if not eq:
        return False, "Equipment not found."
    if out(data, eid):
        return False, "Cannot delete: units are currently borrowed."
    data["equipment"].remove(eq)
    return True, f"Deleted '{eq['name']}'."


def search(data, text):
    t = text.strip().lower()
    return [e for e in data["equipment"] if t in e["name"].lower() or t in e["category"].lower()]


def borrow(data, who, eid, qty):
    eq = find(data["equipment"], eid)
    if not who or not eq or qty < 1:
        return False, "Need a name, a valid equipment ID and a quantity of at least 1."
    free = eq["quantity"] - out(data, eid)
    if qty > free:
        return False, f"Rejected: only {free} unit(s) available."
    tid = data["next_tid"]
    data["next_tid"] += 1
    data["transactions"].append({"id": tid, "equipment_id": eid, "employee": who, "quantity": qty,
                                 "date": str(date.today()), "status": "borrowed"})
    return True, f"Borrowed. Transaction ID: {tid}"


def give_back(data, tid):
    tx = find(data["transactions"], tid)
    if not tx:
        return False, "Transaction not found."
    if tx["status"] == "returned":
        return False, "Already returned. Nothing changed."
    tx["status"] = "returned"
    return True, f"Returned. {tx['quantity']} unit(s) available again."


#MohammedAlnsafi