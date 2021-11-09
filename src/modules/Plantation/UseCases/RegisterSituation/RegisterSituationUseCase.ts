import { PlantationRepository } from "../../Repository/PlantationRepository";

interface RegisterSituationDTO{
    plantingId :String, 
    typeOfIrrigation :String, 
    irrigationDate : Date, 
    weather : Number, 
    moisture: Number
}


class RegisterSituationUseCase {

    constructor(){}

   async execute({plantingId, typeOfIrrigation, irrigationDate, weather,moisture} : RegisterSituationDTO){

    try {

        const repository = new PlantationRepository();

        const date = new Date(irrigationDate)

        const situation = await repository.RegisterSituation(plantingId, typeOfIrrigation, date, weather,moisture)
    
        return situation;
        
    } catch (error) {

        throw new Error(error.message);
        
    }

    }

}


export {RegisterSituationUseCase}