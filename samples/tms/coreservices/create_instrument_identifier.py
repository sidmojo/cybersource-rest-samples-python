from CyberSource import *
import json
import os
import inspect
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def create_instrument_identifier():
    try:
        print("\n[BEGIN] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)
        # Setting the json message body
        request = Body()
        card_info = Tmsv1instrumentidentifiersCard()
        card_info.number = "123456789098765"
        request.card = card_info.__dict__

        processing_info = Tmsv1instrumentidentifiersProcessingInformation()
        authorize_options_info = Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptions()
        initiator = Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptionsInitiator()
        merchant_initiated_info = Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction()
        merchant_initiated_info.previous_transaction_id = "123456789012345"
        initiator.merchant_initiated_transaction = merchant_initiated_info.__dict__
        authorize_options_info.initiator = initiator.__dict__
        processing_info.authorization_options = authorize_options_info.__dict__
        request.processing_information = processing_info.__dict__

        message_body = json.dumps(request.__dict__)
        # Reading Merchant details from Configuration file
        config_obj = configuration.InputConfiguration()
        details_dict1 = config_obj.get_configuration()
        instrument_identifier_obj = InstrumentIdentifiersApi(details_dict1)
        # Calling api_client variable in Configuration file
        config = Configuration()
        print("\nAPI REQUEST BODY: ",
              config.api_client.masking(json.dumps(config.api_client.replace_underscore(json.loads(message_body)))))
        response_data = instrument_identifier_obj.tms_v1_instrumentidentifiers_post(
            "93B32398-AD51-4CC2-A682-EA3E93614EB1", body=message_body)
        # Calling api_client variable in Configuration file
        request_headers = config.api_client.request_headers
        # Statements to print on console
        print("\nAPI REQUEST HEADERS: ", request_headers)
        print("\nAPI RESPONSE CODE : ", response_data.status)
        print("\nAPI RESPONSE BODY : ", response_data.data)
        print("\nAPI RESPONSE HEADERS: ", response_data.getheaders())
        return json.loads(response_data.data)
    except Exception as e:
        print("\nException when calling InstrumentIdentifiersApi->tms_v1_instrumentidentifiers_post: %s\n" % e)
    finally:
        print("\n[END] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)



if __name__ == "__main__":
    create_instrument_identifier()
