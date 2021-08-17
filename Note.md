# Machine Learning Pipelines 

- ML Flow 
    - ML Flow run. Orchestrating flows 
    - main.py 
    - conda.yml 
    - MLproject 
    - download_data
    - remove_duplicates 
    - Conda VS Docker 
        - Isolating the runtime environment of ML Pipeline from host machine  
        - MLflow can use both on CONDA and DOCKER

- Running on Cloud
    - Databricks: MLflow supports Databricks ('-b' option)
    - directly on a single instance ("mlflow run") 
    - Hydra Launchers: Joblib (Parallel), Ray (Cluster) , Redis Queue, SLURM 
    - Kubernetes Cluster (Docker/CONDA)
    - Kubeflow on K8s. 

- Hydra
    - A framework for configuring complex applications 
    - parameters in one or more config files 
    - override from command line 
    - config by a YAML file 
         - "main" section
         - "data" section 
         - "random_forest_pipeline" section 

- Weights and Biases 
- EDA (Exploratory Data Analysis)

- Data Segregation (training/validation/test split)

- Feature Engineering 
    - Feature Store - to reduce the computation in large scale (by avoid recomputing at inference)

- Data Validataion
    - Unit testing for data 
    - To avoid garbage in garbage out 
    - use "pytest" 
        - This is a framework for testing (not only for data validation)
        - need a directory ("/test")
        - File names in the directory need to be "test_XXXX.py" 
        - function names in those files need to be "def test_xxxxx(XX):"
        - functions need to have "assert"s
        - "@pytest.fixture" 
        - "scope='session'"  or "scope='funciton'"  
        - provides options in command line parameters (--input_artifact) 
        - "conftest.py": sharing fixutures all the test. 
        - "pytest.fail()" 
    - Deterministic test/non-deterministic (statistics) test 
        - determiniisitic test. Examples: 
            - number of columns 
            - lengths 
            - categorical values 
            - legal range for variables 
        - non-determnisitic/statistical tests (with some randomness). Examples: 
            - comparison of charasteristics (mean, std, outliers, correlations, distributions) with previous dataset
            - hypothesis testing.
                - null hypothesis: two distributions are the same mean (t-test)
                - alternative hypothesis: different means 
                - t-test. If p-value < 0.05 (reject null, with 2 sigma). p should be decieded previously
            - KS test: test the distribution is the same or not

- Great Expectations 
    - a python based open-source library for validating, documenting, profiling data. Unit testing
    - functions
        - pre-defined tests 
        - automatic profiling 
        - HTML reports 
        - however, it is pretty complex 

- Inference Pipeline 
    - inference artifact is not just a model (because that requires preprocessing)
    - Inference pipeline contains 
        - preprocessing 
        - trained model 
    - Inference pipleline examples: transformer -> transfoermer -> .... -> Model (classifier/regressor)
    - Examples
        - Scikit-learn pipelines 
        - Pytorch script 
    - Feature Store 
    - Exporting inference pipeline 
    - "MLflow models" - isolated environment 
        - MLflow exports => sklearn, pytorch, keras, ONNS, generic python function 
    - to Docker (with API)

- Bringing order to the chaos 
    - version the data
    - version the code - github
    - track every experiment (use Weights and Biases or MLFlow Tracking) 

- Parameter sweeps 
    - Hydra's function 
    - grid of parameters. useful for hyper paramter optimization

- ML Ops
    - should use the same code for development and production. otherwise causes problems 
    - 

- Release 
    - Version Control. simple one: one pipeline one repository
    - Deploy inference artifact with MLflow 
    - Online Vs Offline
        - Online: real time. Latency is important
        - Offline: batch. Throughput (inference on specific time) is important 
    - Other options 
        - Spark - for batch inference  
        - 
