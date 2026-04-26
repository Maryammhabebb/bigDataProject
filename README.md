football-spark-analytics/
│
├── data/
│   ├── raw/                  # original dataset
│   ├── processed/            # cleaned parquet
│
├── notebooks/                # for EDA + visualization
│   ├── 01_eda.ipynb
│   ├── 02_visualization.ipynb
│
├── src/
│   ├── ingestion/            # loading data
│   │   └── ingest.py
│
│   ├── preprocessing/        # cleaning + joins
│   │   └── preprocess.py
│
│   ├── features/             # feature engineering
│   │   └── features.py
│
│   ├── models/               # training
│   │   └── train.py
│
│   ├── evaluation/
│   │   └── evaluate.py
│
│   └── utils/
│       └── spark.py
│
├── outputs/
│   ├── figures/
│   ├── models/
│
├── requirements.txt
├── README.md
└── .gitignore