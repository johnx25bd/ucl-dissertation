

## Key scripts?

Simple voting mechanism to grant access controls to a wallet address (i.e. account owner) (<- not MVP - or is it? The DAO dpki).

Edge scripts to process and store data, ideally with aggregative pruning scripts -  plus edge databases are blockchains (i.e. each state contains the prior state's merkle root hash) (<- not MVP).

Request from device. Essentially includes authentication and request parameters (i.e. query parameters).
  Can indicate for device to write, if permissioned appropriately.
Response from edge device, if warranted.
  Does this require a contract call? I think so, at least for high-security situationss (in which access controls might be updated rapidly. Included in access grant is an expiry time, and some indicator as to how long a device can be offline and still grant access to a particular EOA.)




1. JS - GET request? With signature? Device requests data. Request is propagated to target device. No need for contract call.
2. Target (edge - in this case server) device handles call.
  1. Verifies sender signature / message integrity.
  2. Transmits transaction to vm with requestor, time, location (?), some indication of level of access requested. Web3.js.
  4. VM contract invocation accesses current state of the chain - `mapping (address=>permissions) x;`,
  ```

    location struct {

    }
    CurrentPermissions struct {
      //
    };

    PermissionRequest struct {
      address requestor;
      int[2] currentLocation; // [float lon * 1000000, float lat * 100000]
      

    }


    fetchPermissions (
      address _requestor,
      PermissionRequest _permissions)
      public ( returns boolean granted_ ) {

        CurrentPermissions = x[address];

        if (accepted(PermissionRequest, CurrentPermissions)) {
          return true;
        } else {
          return false;
        }

    }
  ```
  3.
