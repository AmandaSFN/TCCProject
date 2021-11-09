import { GetPlantationUseCase } from "./GetPlantationUseCase";






class GetPlantationController {

    constructor(){

    }


    async handle(req: Request, res: Response){

        const {id} = req.headers

        const getPlantationUseCase = new GetPlantationUseCase();

        try {

            const plantation = await getPlantationUseCase.execute(id)

            return res.status(200).json(plantation);
            
        } catch (error) {
            return res.status(500).json({message: error.message});


            
        }
    }


}


export {GetPlantationController}