head = """
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Financial Summary</title>
    <style>
        .logo {
            width: 100px;
        }
        body {
            font-family: Arial, sans-serif;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
"""


def get_email_template(total: float, avg_debt: float, avg_credit: float, transactions: str):
    return """
                <!DOCTYPE html>
                <html lang="en">
                 {head}
                <body>
                    <h2>Financial Summary</h2>
                    <img src="https://res.cloudinary.com/deirp9aws/image/upload/v1711218361/logo_ilskmc.png" alt="Logo de tu empresa" class="logo">
                    <table>
                        <tr>
                            <th>Dato</th>
                            <th>Valor</th>
                        </tr>
                        <tr>
                            <td>Total Balance</td>
                            <td>{total}</td>
                        </tr>
                        <tr>
                            <td>Average Credit Amount</td>
                            <td>{avg_credit}</td> 
                        </tr>
                        <tr>
                            <td>Average Debit Amount</td>
                            <td>{avg_debt}</td>
                        </tr>
                        <tr>
                            <td>Number of Transactions</td>
                            <td>
                                <ul>
                                    {transactions}
                                </ul>
                            </td>
                        </tr>
                    </table>
                </body>
                </html>
                """.format(head=head, total=total, avg_debt=avg_debt, avg_credit=avg_credit, transactions=transactions)
