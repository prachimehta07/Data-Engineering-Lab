import re

def validate_customer(row):
    errors = []

    if row.get("email") is None or row.get("email") == "":
        errors.append("missing email")
    elif not re.match(r"^[^@]+@[^@]+\.[^@]+$", str(row.get("email"))):
        errors.append("invalid email format")

    phone = str(row.get("phone", ""))
    if phone == "" or phone == "None":
        errors.append("missing phone")
    elif len(phone) != 10 or not phone.isdigit():
        errors.append("invalid phone")

    age = row.get("age")
    if age is None or age < 18 or age > 100:
        errors.append("invalid age")

    if not row.get("name"):
        errors.append("missing name")

    return errors

def validate_product(row):
    errors = []

    if row.get("price") is None or row.get("price") <= 0:
        errors.append("invalid price")

    if not row.get("product_name"):
        errors.append("missing product name")

    if row.get("category") is None:
        errors.append("missing category")

    return errors

def validate_transaction(row):
    errors = []

    amount = row.get("payment.amount")
    if amount is None or amount <= 0:
        errors.append("invalid amount")

    method = row.get("payment.method")
    if method not in ["UPI", "CARD", "NETBANKING", "COD"]:
        errors.append("invalid payment method")

    if row.get("customer.id") is None:
        errors.append("missing customer id")

    return errors

def check_duplicates(df, id_column):
    return df[id_column].duplicated(keep=False)

def separate_valid_invalid(df, validate_func, id_column=None):
    valid_rows = []
    invalid_rows = []

    dup_mask = check_duplicates(df, id_column) if id_column else None

    for idx, row in df.iterrows():
        errors = validate_func(row)

        if dup_mask is not None and dup_mask[idx]:
            errors.append("duplicate id")

        if errors:
            record = row.to_dict()
            record["error_reason"] = "; ".join(errors)
            invalid_rows.append(record)
        else:
            valid_rows.append(row.to_dict())

    return valid_rows, invalid_rows