=============================
Seriously Homework Assignment
=============================

This is a possible implementation for the following problem:

* Create a software design for a basic vending machine. Write the specs and desired functionalities. We're interested only in the functional design, not the visual/physical design (no UI is necessary).
* Use the programming language of your choice to implement the virtual vending machine you designed. Demonstrate your understanding of object-oriented design and good coding practices.
* Write a command-line test program that allows a user to test your vending machine. The user should be able to see a list of snacks/prices, select a snack, put money into the machine, receive money back, etc.

---------------

Q1: Software design
===================

Features of the abstract vending machine should include (considering one pictured `here <https://5.imimg.com/data5/IN/BV/MY-3410170/candy-bar-vending-machine-500x500.png>`_):

* should have certain number of slots for products
* each channel / slot has certain fixed-sized depth for products
* each slot is loaded with a stock of single type of product
* multiple slots can be loaded with the same type of product
* vending machine features a single payment method

An abstract product has two basic features:

* name / description
* price

A payment process consists of 3 steps:

#. balance is set, payment initiated
#. payments made until there is outstanding balance
#. give back money if balance is negative

In case of a card payment, the last step never happens as only precise payments should be possible. A payment should be either successful or possible to be cancelled in which case the already made payments should be returned.

Q2: Implementation notes
========================

* Product is defined as an abstract class which the current features do not require, but might have impact with other modules / usecases
* For simplification reasons, for cash payments, the possible note / coin values were not considered, neither cash in the machine
* Payment issues (card transaction, etc) were not considered this time

Q3: Command line test UI
========================

Code sample for machine setup can be found in test.py file

Purchase process consists of following steps:

#. List of available products observed
#. Choice is made and slot code entered
#. Payment made / Payment cancelled

Payment conclusion or any error during the process clears the product selection. Purchase can be cancelled by typing "CANCEL".
Vending machine is operational as long as it is unplugged. You can unplug the test script by typing CTRL+C. :)
