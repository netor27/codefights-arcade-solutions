def htmlTable(table, row, column):
    rows = table.split("<tr>")
    if len(rows) <= row+1:
        return "No such cell"
    thisRow = rows[row+1]
    cols = thisRow.split("<td>")
    if len(cols) <= column + 1:
        return "No such cell"
    data = cols[column+1]
    return data.replace("</table>", "").replace("</td>", "").replace("</tr>", "")

