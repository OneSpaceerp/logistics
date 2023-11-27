from frappe import _

def get_data():
	return {
		'fieldname': 'booking_order',
		'transactions': [
			{
				'items': ['Stock Entry', 'Timesheet']
			}
		]
	}