from shire.models import DNA_EXTRACTS

COLUMNS = 8

def combine(sheet_rows, scan):
    expected = {d.POSITION: d for d in sheet_rows}
    result = []
    for tube in sorted(scan["tubeBarcode"], key=lambda t: (t["row"], t["column"])):
        pos = (tube["row"] - 1) * COLUMNS + tube["column"]
        det = expected.pop(pos, None)
        barcode = tube.get("barcode")
        on_sheet = bool(det and det.LABNO)

        if tube["decodeStatus"] not in ("SUCCESS", "EMPTY"):
            problem = "Barcode could not be read"
        elif on_sheet and not barcode:
            problem = "Sample on sheet but no tube in rack"
        elif barcode and not on_sheet:
            problem = "Tube in rack but not on sheet"
        else:
            problem = ""

        result.append({"position": pos, "row": tube["row"], "column": tube["column"],
                       "labno": det.LABNO if det else None,# "tube": det.TUBE if det else None,
                       "barcode": barcode, "problem": problem})

    # Sheet positions that don't exist in the scanned rack
    for det in expected.values():
        result.append({"position": det.POSITION, "labno": det.LABNO, #"tube": det.TUBE,
                       "barcode": None, "problem": "Position not in scanned rack"})
    return result

def extractsheet(extractSheetList, scan):

    sql = """select E.EXTRACTION_METHOD, D.POSITION, ROW, [COLUMN], E.LABNO, E.TUBE, TUBE_BARCODE, RACK_BARCODE from DNA_EXTRACTS E
            LEFT JOIN DNA_EXTRACTSHEET_DET D on E.LABNO = D.LABNO and E.TUBE = D.TUBE
            LEFT JOIN LINQ_FORMATS L on D.POSITION = L.POSITION_ID and E.EXTRACTION_METHOD = L.EXTRACTION_METHOD
            where EXTRACT_SHEET = %s
            ORDER BY POSITION
        """
    extractsheet = list(DNA_EXTRACTS.objects.raw(sql, ["100240"]))

    barcodes = sorted(scan["tubeBarcode"], key=lambda t: (t["column"], t["row"]))

    result = []

    for sample in extractsheet:
        print(sample.POSITION, ", ", sample.ROW, ", ", sample.COLUMN)

    return result
