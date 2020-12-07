# Predicting Protein Docking Sites
Amanda Beck and Daniel Goodwin
Class project for 6.883, Autumn 2020

## Overview
This code uses the ProteinGCN code as a base to work on the protein docking problem. Our hypothesis was tht the ProteinGCN network, trained on the Rosetta300k datset, would give a good embedding to learn the docking sites between two proteins. This hypothesis ended up being disproven, for our code, there was no performance difference between the embedded and non-embedded proteins.

## To run the code
- We convert the data into a loadable format using the notebook "Saving DB5 into loadable format"
- We build the siamese/RelNet in "RelationNet on ProteinGCN to Predict Binding"
- We explored using an autoencoder for a more global view of docking in "Final - AE Code"

## Thanks
Big thanks to Iddo Drori, TA Zee Yan, and the class of 6.883 in Autumn 2020

