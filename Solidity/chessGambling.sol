// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract ChessBetting is FunctionsConsumer {
    function commitGame(
        string memory matchID,
        address opponenet
    ) public payable returns (bool success) {}

    function requestPayoutWinner(
        string memory matchID
    ) public returns (bool success) {
        // Send chainlink functions https request to get match results
    }

    function resolvePaytoutWinner(
        bytes32 requestId,
        bytes memory response,
        bytes memory err
    ) {
        // Parse response and send payout to winner
        // Gracefully handle errors, such as matchID not found, or match not finished
    }
}
