import React from 'react'
import { Link } from 'react-router-dom';

const PostItem = ({ post }) => {

    return (
        <div className="w3-card-4 w3-margin w3-white">
            <img src={post.image} alt={post.title} className="post-img" />
            <div className="w3-container">
                <h3><b>{post.title}</b></h3>
                <h5><span className="w3-opacity">{post.date}</span></h5>
            </div>

            <div className="w3-container">
                <p dangerouslySetInnerHTML={{ __html: post?.excerpt }}></p>
                <div className="w3-row">
                    <div className="w3-col m8 s12">
                        <Link to={`/blog/${post.slug}/`}>
                            <p><button className="w3-button w3-padding-large w3-white w3-border"><b>READ MORE »</b></button></p>
                        </Link>
                    </div>
                    <div className="w3-col m4">
                        <Link to={`/blog/${post.slug}/#comments`}>
                            <p><span className="w3-button w3-padding-large w3-right"><b>Comments &nbsp;</b> <span className="w3-tag">{post.comments_count}</span></span></p>
                        </Link>
                    </div>
                </div>
            </div>
            <hr />
        </div>
    );
}

export default PostItem;
