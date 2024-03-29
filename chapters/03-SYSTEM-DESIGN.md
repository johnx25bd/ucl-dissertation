
## Requirements

Security  

Integrity

Low energy / compute / storage resources at the edge.

Interoperability

Forward secrecy (?)


## Outline

Governing the informational commons - a decentralized approach.

A self organizing system for data governance.

Information is a non-rivalrous good - use by one individual does not reduce availability to others (Allen 2015).

The reverse tragedy of the commons: not sharing a good that  would benefit the public because there is no cost to remaining private, and  possibly some cost to making it public (i.e. a competitor can access and leverage).

  Technical reasons: data formats, lack of interoperability
  Socioeconomic reasons: Lack of incentivization to share, cost to configure interoperable system.

  Solution: Precompetitive coordination to define common protocol, plus some incentivization structure to encourage participation. Perhaps simply sharing data grants you access to the data ocean.

"Information age assets don't follow industrial age scarcity principles. They GROW in value when shared. If Info Age economies don't revolve around scarcity, then we need new models." (http://www.artbrock.com/presentations/new-economy-new-wealth)


Zero knowledge proofs to demonstrate possession of data w ithout revealing informational content?


Principle of subsidiarity - aka Govern Locally (Allen 2015) - "Community self-determination is recognized and supported by higher-level authorities."

"Effective human relationships" > "A faceless authority".

Questions:

What factors are influenced by the scal of operation? What are the optimal scales for each "sphere of activity." (Allen 2015).

"Large scale governance requires finding the optimal scale for each sphere of activity and appropriately coordinating the activities, a concept called polycentric governance."

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

Public office in France.

  3.
