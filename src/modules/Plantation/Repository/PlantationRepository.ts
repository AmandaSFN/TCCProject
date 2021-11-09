import { Plantation } from "../entity/Plantation";

import {getRepository, Repository} from "typeorm";
import { PlantingSituation } from "../entity/PlantingSituation";




class PlantationRepository{

    
    private repository: Repository<Plantation>

    constructor(){

        this.repository = getRepository(Plantation)

    }



    async CreatePlantation(NamePlantation : String) : Promise<Plantation>{

        const plantation = new Plantation(NamePlantation)

        await this.repository.createQueryBuilder()
        .insert()
        .into(Plantation)
        .values([plantation])
        .execute();

        

        return plantation;

        
    }

    async RegisterSituation(plantingId, typeOfIrrigation, irrigationDate, weather,moisture) : Promise<PlantingSituation>{

        const plantingSituation = new PlantingSituation(plantingId, typeOfIrrigation, irrigationDate, weather,moisture)

        await this.repository.createQueryBuilder()
        .insert()
        .into(PlantingSituation)
        .values([plantingSituation])
        .execute();

        

        return plantingSituation;

        
    }


    async GetSituation(id:String): Promise<UNKNOWN>{

        const repository = getRepository(PlantingSituation)

        const situations = await repository
        .createQueryBuilder()
        .where("PlantingSituation.plantingId = :id",{id:id})
        .execute()


        return situations;
    }



    async GetPlantation(id:String): Promise<UNKNOWN>{

       

        const plantation = await this.repository
        .createQueryBuilder()
        .where("id = :id",{id:id})
        .getOne();


        return plantation;

    }
}


export {PlantationRepository}