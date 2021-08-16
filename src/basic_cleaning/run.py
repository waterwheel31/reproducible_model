#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact 
"""
import argparse
import logging
import wandb
import pandas as pd


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)
    
    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
     

    ######################
    # YOUR CODE HERE     #
    ######################
    
    logger.info("Fetching artifact")
    artifact_local_path = run.use_artifact(args.input_artifact).file()
    
    print(artifact_local_path)
    
    
    logger.info("Reading dataframe")
    df = pd.read_csv(artifact_local_path)
    
    logger.info("Starting pre-processing")
    df = df.drop_duplicates().reset_index(drop=True)
    
    minPrice = args.min_price
    maxPrice = args.max_price
    
    df = df[(df['price'] >= minPrice) & (df['price'] <= maxPrice)]
    
    idx = df['longitude'].between(-74.25, -73.50) & df['latitude'].between(40.5, 41.2)
    df = df[idx].copy()
    
    outfile = args.output_artifact
    df.to_csv(outfile)
    
    artifact = wandb.Artifact(
        name=args.output_artifact,
        type=args.output_type,
        description=args.output_description,
        )
    
    artifact.add_file("clean_sample.csv")
    run.log_artifact(artifact)  # uploaded at this step 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")


    parser.add_argument(
        "--input_artifact", 
        type=str,
        help="name of the input artifact",
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type=str,
        help="name of the output artifact",
        required=True
    )

    parser.add_argument(
        "--output_type", 
        type=str,
        help="type of the output",
        required=True
    )

    parser.add_argument(
        "--output_description", 
        type=str,
        help="output description",
        required=True
    )

    parser.add_argument(
        "--min_price", 
        type=float,
        help="minimum price",
        required=True
    )

    parser.add_argument(
        "--max_price", 
        type=float,
        help="maximum price",
        required=True
    )


    args = parser.parse_args()

    go(args)
