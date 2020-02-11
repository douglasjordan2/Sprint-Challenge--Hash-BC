# Sprint Challenge: Hash Tables and Blockchain

This challenge allows you to practice the concepts and techniques learned over the past week and apply them in a concrete project. This Sprint, we learned how hash tables combine two data structures to get the best of both worlds and were introduced into the fascinating world of blockchains. In your challenge this week, you will demonstrate proficiency by solving algorithms in Python using hash tables and add another key feature to your blockchain.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your work reflects your proficiency in Python and your command of the concepts and techniques in related to hash tables and blockchains.

You have three hours to complete this challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons and your project manager.

## Description

This sprint challenge is divided up into three parts:  Hash tables coding, blockchain coding, and a short interview covering parts of hash tables and blockchain.

## Interview Questions

Explain in detail the workings of a dynamic array:
* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?
* What is the worse case scenario if you try to extend the storage size of a dynamic array?

Since items in an array are indexed and can be accessed immediately by retrieving the value by its index, the time complexity to access them is always O(1). Adding or removing an item to the front of an array requires shifting the position of all subsequent values by 1 position, so the time complexity for these operations is O(n). Conversely, adding or removing items from the back of an array doesn't require the shifting of the other elements, so the time complexity is just O(1). The worst case scenario for extending an array is doubling its size. Doubling the size of an array implies appending an item for each item in the array. The time complexity for this operation is therefore O(n).

Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?
A blockchain is a tough concept to describe, but the term 'blockchain' is a pretty succinct description of its structure. The 'chain' is the structure that contains all of the transactions recorded. Each block is a link in the chain, and these blocks hold important information. This information includes the block's index within the chain, a timestamp of when it was created, transactions that are proofed by the block, and the hash for the previous block within the chain. Consensus is determined by the longest valid chain. This is important, because if someone were to try and modify a block in the middle of the chain, the previous hash value for the next block in the chain would no be valid. It would be impossible for someone to modify the block, then recreate all the subsequent blocks and still have the longest valid chain, because other people are busy adding to the longest valid chain. This is why each block needs proof of work.
 
Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?
Proof of work operates by making it arbitrarily difficult to search for the next block, but easy for the rest of the network to validate it. When a block is found, the hash from the previous block is added to it and this data is shared to the nodes in the network. These nodes verify the block has an index one higher than the block that was previously last on the chain, and verify the previous hash stored in the new block. This protects the chain from attack, because modifying a block in the middle of the chain would require rebuilding all subsequent blocks. Because everyone is busy mining and adding blocks to the chain, the cheater would have to expend exponentially more effort than everyone else in the network to try and pass their modified chain off as the valid one. Even if they attempted this, the previous hash on the block following the modified block would no longer be valid, so the network would reject this blockchain as invalid. If they simply cut the chain at the bad hash, the chain would no longer be the longest one so it would again get rejected.

I had to research what kinds of attacks are possible on a blockchain, and it appears that DDoS attacks are common. Overwhelming the blockchain networks' resources can allow hackers disconnect and take over mining pools, e-wallets, exchanges, etc. Many blockchain networks have safeguards in place to prevent DDoSing. Other types of attack appear to mainly target individual users of blockchain technology, for example by tampering with transactions before the transaction is broadcast to the network. If a hacker can manage to alter a transaction ID and broadcast it to the network in time for it to be confirmed before the original transaction, they can successfully withdraw the funds of that transaction.

## Project Set Up

#### [Hash Tables]

For the hash tables portion of the sprint challenge, you'll be working through two algorithm problems that are amenable to being solved efficiently using a hash table. You know the drill at this point. Navigate into each exercise's directory, read the instructions for the exercise laid out in the README, implement your solution in the .py skeleton file, then make sure your code passes the tests by running the test script with make tests.

A hash table implementation has been included for you already. Your task is to get the tests passing (using a hash table to do it). You can remind yourself of what hash table functions are available by looking at the hashtable.py file that is included in each exercise directory (note that the hash table implementations for both exercises differ slightly).

*You may not use any advanced, built-in Python functions to solve these problems.*

#### [Blockchain]

For the blockchain portion of the challenge, you will be writing code for a new miner that will solve a different Proof of Work algorithm than the one we have been working with.

Your goal is to mine at least one coin.  Keep in mind that with many people competing over the same coins, this may take a long time.  By our math, we expect that an average solution should be the first to find a solution at least once in an hour or two of mining.  

## Minimum Viable Product

#### [Hash Tables](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/hashtables)

#### [Blockchain](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/blockchain)


### Rubric

| *OBJECTIVE*                                                                                                     | *TASK*             | *1 - DOES NOT MEET EXPECTATIONS*                                                                                            | *2 - MEETS EXPECTATIONS*                                                                                                       | *3 - EXCEEDS EXPECTATIONS                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| implement and describe how high-level array functions work down to the memory level                             | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
| implement and utilize basic hash table + handle collisions and resizing in a hash table                         | Hash Problem 1 & 2 | Tests do not pass on one or both problems, or solutions do not use hash tables.                                             | Tests pass on both problems.  Solution utilizes a hash table.                                                                  | Tests pass on on both problems with solutions utilizing hash tables, linear runtime complexity, no flake8 complaints.                                 |
| diagram and code a simple blockchain, utilizing a cryptographic hash                                            | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
| utilize a Proof of Work process to protect a blockchain from attack                                             | Blockchain Problem | The student is unable to mine a coin before the end of lunch.                                                               | The student was able to mine a coin before the end of lunch.                                                                   | The student presented a unique solution that was able to mine more than 100 coins before the end of lunch.                                            |
| build a protocol to allow nodes in a blockchain network to communicate to share blocks and determine consensus. | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
