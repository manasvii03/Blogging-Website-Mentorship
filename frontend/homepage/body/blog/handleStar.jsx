import react, {useState} from 'react';
import API from '../../baseURL/baseURL';
function Star({blogId}){
    const [starred,setStarred]=useState(false);
    const handleStarred=async ()=>{
        const user_token = localStorage.getItem('token');
        try{
            setStarred(!starred);
            await API.post(`/blogs/${blogId}/star/`, {}, {
            headers: {
               'Authorization': `Token ${user_token}`, 
          'Content-Type': 'application/json'}});
        }
        catch(err){
            console.log(`Error: ${err.message}`);
        }
    }
    return(
        <div className="star"><button className="starBtn2" onClick={handleStarred}><svg className={starred?"starred":"notstarred"} viewBox="0 0 48 48" fill="none" height="30" width="30"><path d="M24 4L30.18 16.52L44 18.54L34 28.28L36.36 42.04L24 35.54L11.64 42.04L14 28.28L4 18.54L17.82 16.52L24 4Z"/></svg></button></div>
    );
}
export default Star;