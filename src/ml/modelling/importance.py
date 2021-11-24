import sys
sys.path.append('..')
sys.path.append('../..')
import matplotlib.pyplot as plt
import shap
import ml.data.utils.f1_categorical_transformations as f1_categorical_transformations

def run_importance(clf, train_x, out_path='plots/importance.png'):
    explainer = shap.Explainer(clf)
    shap_values = explainer.shap_values(train_x)

    asia_mapper = f1_categorical_transformations.get_ordinal_features()['ASIA - Discharge']
    reverse_asia_mapper = {v: k for k, v in asia_mapper.items()}
    classes = [reverse_asia_mapper.get(x, x) for x in clf.classes_]
    
    shap.summary_plot(shap_values, feature_names=list(train_x.columns.values), class_names=classes, plot_size=(44, 22), show=False)
    plt.savefig(out_path)
