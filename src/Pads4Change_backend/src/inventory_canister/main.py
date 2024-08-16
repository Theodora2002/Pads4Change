from kybra import ic, nat, query, update, stable, Variant, Principal

class InventoryItem(stable):
    item_name: str
    quantity: nat

inventory: dict[str, InventoryItem] = {}

@update
def add_item(item_name: str, quantity: nat) -> bool:
    if item_name in inventory:
        inventory[item_name].quantity += quantity
    else:
        inventory[item_name] = InventoryItem(item_name=item_name, quantity=quantity)
    return True

@update
def allocate_items(school_id: str, quantity: nat) -> bool:
    if "sanitary_pads" in inventory and inventory["sanitary_pads"].quantity >= quantity:
        inventory["sanitary_pads"].quantity -= quantity
        ic.call_other_canister(
            Principal.from_str(school_id),
            "receive_items",
            [inventory["sanitary_pads"].item_name, quantity]
        )
        return True
    return False

@query
def check_inventory() -> dict[str, InventoryItem]:
    return inventory
