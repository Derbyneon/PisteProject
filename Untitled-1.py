from hestage.models import Stage

stage_data = Stage.objects.all()
for stage in stage_data:
    print(stage.id_stage, stage.nom_stage, stage.nom_entreprise)
