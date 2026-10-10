from imblearn.over_sampling import SMOTE
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import average_precision_score
from sklearn.model_selection import train_test_split

def test_training_stack_runs():
    X, y = make_classification(
        n_samples=2000, n_features=10, weights=[0.95, 0.05], random_state=42
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    X_res, y_res = SMOTE(random_state=42).fit_resample(X_train, y_train)
    assert len(y_res) > len(y_train)

    model = RandomForestClassifier(n_estimators=20, random_state=42)
    model.fit(X_res, y_res)

    probs = model.predict_proba(X_test)[:,1]
    assert 0.0 <= average_precision_score(y_test, probs) <= 1.0