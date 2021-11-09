import {Response , Request} from 'express'
import { CreatePlantationUseCase } from './CreatePlantationUseCase';


class CreatePlantationController{


    constructor(){}


    async handle(req: Request, res : Response): Promise<Response> {
        const {namePlantation} = req.body

        try {

            const createPlantationUseCase = new CreatePlantationUseCase();

           const plantation =  await createPlantationUseCase.execute(namePlantation)
           res.json({"Name": plantation.namePlantation, "id" : plantation.id}).status(201);
            
        } catch (error) {

            throw new Error(error.message)
            
        }
    }
}


export {CreatePlantationController}