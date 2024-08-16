from kybra import query, update, nat, stable, Principal

class DistributionRecord(stable):
    school_id: Principal
    item_name: str
    quantity: nat

distribution_records: list[DistributionRecord] = []

@update
def receive_items(item_name: str, quantity: nat) -> bool:
    distribution_records.append(
        DistributionRecord(school_id=ic.caller(), item_name=item_name, quantity=quantity)
    )
    return True

@query
def get_distribution_records() -> list[DistributionRecord]:
    return distribution_records

