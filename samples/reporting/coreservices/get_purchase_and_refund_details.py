from CyberSource import *
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def purchase_and_refund():
    try:
        start_time = "2018-05-01T12:00:00-05:00"
        end_time = "2018-05-30T12:00:00-05:00"
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        purchase_refund_obj = PurchaseAndRefundDetailsApi(details_dict1)
        return_data, status, body = purchase_refund_obj.get_purchase_and_refund_details(start_time, end_time)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)

    except Exception as e:
        print("Exception when calling PurchaseAndRefundDetailsApi->get_purchase_and_refund_details: %s\n" % e)


if __name__ == "__main__":
    purchase_and_refund()
