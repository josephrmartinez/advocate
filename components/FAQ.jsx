export default function FAQ({question, answer}) {
    return (
        <div className="my-6">       
            <p className="text-gray-500 font-semibold text-3xl mb-2">
                {question}
            </p>

            <p className="text-gray-700 font-medium text-xl">
                {answer}
            </p>
        </div>
    )
}