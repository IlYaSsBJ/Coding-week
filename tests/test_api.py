from controller.predict import predict_obesity # type: ignore

def test_prediction():
    """Test d'une prédiction avec des valeurs valides"""
    features = {
        "Age": 30, "Height": 1.80, "Weight": 80,
        "Activity": 2, "Food_Intake": 2, "Vegetables": 3, "Water_Intake": 2, "Smoking": 0
    }
    prediction = predict_obesity(features)
    valid_classes = ["Poids Insuffisant", "Poids Normal", "Surpoids Niveau I", 
                     "Surpoids Niveau II", "Obésité Type I", "Obésité Type II", "Obésité Type III"]
    
    assert prediction in valid_classes, f"⚠ Prédiction invalide : {prediction}"

