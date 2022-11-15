def open_text_document(doc_name):
    with open(doc_name, "r+", encoding="UTF-8") as rw_file:
        doc = rw_file.read()

    return doc


def get_info_from_document(doc):
    info = doc.split(":")
    return info


def write_text_to_document(doc):
    print(doc)



