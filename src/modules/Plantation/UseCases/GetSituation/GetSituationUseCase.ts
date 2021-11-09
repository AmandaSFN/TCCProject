
import { PlantationRepository } from "../../Repository/PlantationRepository";



class GetSituationUseCase{

    private repository : PlantationRepository


    constructor(){
        this.repository  = new PlantationRepository();
    }



   async execute(id:String) : Promise<JSON>{

        try {

            const situations  = await this.repository.GetSituation(id)


            return situations
            
        } catch (error) {

            throw new Error(error.message);
            
        }
    }
}


export {GetSituationUseCase}