import { PlantationRepository } from "../../Repository/PlantationRepository";
import {exec} from 'child_process';
import {util} from 'util';






class GetPlantationUseCase{


    constructor(){}


    async teste(): Promise<void>{

        return new Promise<void>((resolve, reject) =>{

           

        })
       
        

}

    async execute(id : String) : Promise<Plantation>{
        //COLOCAR O CAMINHO COMPLEO

        exec('python ./src/modules/Plantation/UseCases/GetPlantation/Main.py', (error, stdout, stderr) => {

            if(error) {
                console.log(error.message);
                
            }
    
            if(stdout){
                console.log(stdout)

            }
    
            if(stderr){
                console.log(stderr)
            }

    })

        const repository = new PlantationRepository();

        try {
            const plantation =  await repository.GetPlantation(id)
            const situations = await repository.GetSituation(id);

            return {situations, plantation}
        } catch (error) {
            
        }

    }
}


export{GetPlantationUseCase}