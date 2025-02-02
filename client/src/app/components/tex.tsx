import ReactMarkdown from "react-markdown";
import { FC } from "react";
import "katex/dist/katex.min.css"; // If you want to keep LaTeX support

const MarkdownRenderer: FC<{ markdown: string | undefined }> = ({
  markdown,
}) => {
  return <ReactMarkdown children={markdown} />;
};

export default MarkdownRenderer;
