import { GetSituationUseCase } from "./GetSituationUseCase";








class GetSituationController{

    constructor(){

    }


    async handle(req: Request, res: Response){

        const getSituations = new GetSituationUseCase();

        const {id} = req.headers

        try {

            const situations  = await getSituations.execute(id)


            return res.status(200).json(situations);
            
        } catch (error) {
            
            return res.status(400).json({"error": error.message})
        }

    }
}


export {GetSituationController}